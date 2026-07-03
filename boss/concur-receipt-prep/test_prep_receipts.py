#!/usr/bin/env python3
"""Unit tests for the OCR-parsing / naming core (no macOS deps needed).

Run:  python3 test_prep_receipts.py
"""
import datetime as dt
import unittest

import prep_receipts as p


SAMPLE = """\
STARBUCKS STORE #1234
123 Main St, Seattle WA
Order #44
05/12/2026  10:32 AM

Grande Latte        5.45
Croissant           3.50
Subtotal            8.95
Tax                 0.81
Total              $9.76

VISA ****1234
Thank you!
"""


class ParseTests(unittest.TestCase):
    def test_date_us_slash(self):
        self.assertEqual(p.parse_date(SAMPLE), "2026-05-12")

    def test_date_iso(self):
        self.assertEqual(p.parse_date("Date: 2026-05-12"), "2026-05-12")

    def test_date_textual(self):
        self.assertEqual(p.parse_date("Jan 5, 2026"), "2026-01-05")
        self.assertEqual(p.parse_date("5 Mar 2026"), "2026-03-05")

    def test_date_dd_mm_disambiguation(self):
        # 25 can't be a month -> must be the day.
        self.assertEqual(p.parse_date("25/03/2026"), "2026-03-25")

    def test_amount_prefers_total_over_subtotal(self):
        self.assertEqual(p.parse_amount(SAMPLE), "9.76")

    def test_amount_fallback_to_largest(self):
        txt = "Item A 4.00\nItem B 12.34\nItem C 1.00"
        self.assertEqual(p.parse_amount(txt), "12.34")

    def test_amount_with_thousands(self):
        self.assertEqual(p.parse_amount("TOTAL $1,234.56"), "1234.56")

    def test_vendor_top_line(self):
        self.assertEqual(p.parse_vendor(SAMPLE), "STARBUCKS STORE #1234")

    def test_sanitize_vendor(self):
        self.assertEqual(p.sanitize_vendor("STARBUCKS STORE #1234"), "StarbucksStore")
        self.assertEqual(p.sanitize_vendor("Joe's Diner & Co."), "JoesDinerCo")
        self.assertEqual(p.sanitize_vendor("WHOLE FOODS MARKET 10412"), "WholeFoodsMarket")

    def test_sanitize_keeps_short_brand_numbers(self):
        # Long numbers = store/register IDs (drop); short numbers = part of the name (keep).
        self.assertEqual(p.sanitize_vendor("7 ELEVEN"), "7Eleven")
        self.assertEqual(p.sanitize_vendor("5 Guys Burgers"), "5GuysBurgers")
        self.assertEqual(p.sanitize_vendor("6003 Kiosk"), "Kiosk")
        self.assertEqual(p.sanitize_vendor("Starbucks Coffee #53313"), "StarbucksCoffee")

    def test_sanitize_preserves_mixed_case_brands(self):
        self.assertEqual(p.sanitize_vendor("UCHealth"), "UCHealth")
        self.assertEqual(p.sanitize_vendor("McDonald's"), "McDonalds")

    def test_vendor_number_leading_name_over_address(self):
        # 7-Eleven: the name starts with a digit and the address line does too.
        # Must pick the brand, not the city/ZIP line below it.
        txt = ("7 ELEVEN\n"
               "310 W UINTAH ST\n"
               "COLORADO SPRINGS CO 809051045\n"
               "Ph: 7196350253\n")
        self.assertEqual(p.parse_vendor(txt), "7 ELEVEN")

    def test_vendor_skips_street_and_phone(self):
        txt = ("2101 Transformation Dr.\n"
               "Lincoln, NE 68508\n"
               "(531) 300-6300\n"
               "SCARLET HOTEL\n")
        # First real name line wins; address/phone above a name are skipped.
        self.assertEqual(p.parse_vendor(txt), "SCARLET HOTEL")

    def test_vendor_number_leading_kiosk(self):
        self.assertEqual(p.parse_vendor("6003 Kiosk\nCHK 5839\n"), "6003 Kiosk")

    def test_build_filename_full(self):
        rec = p.Receipt(source=p.Path("x.heic"))
        rec.out_path = p.Path("x.jpg")
        rec.date, rec.vendor, rec.amount = "2026-05-12", "Starbucks", "9.76"
        self.assertEqual(p.build_filename(rec, 1), "2026-05-12_Starbucks_$9.76.jpg")

    def test_build_filename_fallback(self):
        rec = p.Receipt(source=p.Path("x.heic"))
        rec.out_path = p.Path("x.jpg")
        rec.date = "2026-05-12"  # have date but no vendor/amount
        self.assertEqual(p.build_filename(rec, 3), "2026-05-12_receipt_3.jpg")

    def test_build_filename_fallback_no_date(self):
        rec = p.Receipt(source=p.Path("x.heic"))
        rec.out_path = p.Path("x.jpg")
        self.assertEqual(p.build_filename(rec, 7), "0000-00-00_receipt_7.jpg")

    def test_default_month_label_is_previous_month(self):
        self.assertEqual(p.default_month_label(dt.date(2026, 6, 1)), "2026-05")
        self.assertEqual(p.default_month_label(dt.date(2026, 1, 1)), "2025-12")


if __name__ == "__main__":
    unittest.main(verbosity=2)
