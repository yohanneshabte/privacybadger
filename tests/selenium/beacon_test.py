#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest

import pbtest


class BeaconTest(pbtest.PBSeleniumTest):
    """Tests to make sure beacon detection works as expected."""

    def test_beacon_detection(self):
        PAGE_URL = (
            "https://gitcdn.link/cdn/ghostwords/"
            "be9de3acae16aa832a271ba97fce0073/raw/f2554fbf93faca1bfa397ae610e01bab47bd19b5/"
            "privacy_badger_beacon_test_fixture.html"
        )
        BEACON_DOMAIN = "dnt-test.trackersimulator.org"

        # visit the page
        self.load_url(PAGE_URL)

        # check that we detected the beacon domain as a tracker
        self.load_url(self.options_url)
        self.find_el_by_css('a[href="#tab-tracking-domains"]').click()
        self.driver.find_element_by_id('show-tracking-domains-checkbox').click()
        # filter the list because otherwise our slider may not be in view
        self.driver.find_element_by_id('trackingDomainSearch').send_keys(BEACON_DOMAIN)
        action = self.get_domain_slider_state(BEACON_DOMAIN)
        self.assertEqual(action, "allow",
            "Beacon domain should have been detected as a tracker")


if __name__ == "__main__":
    unittest.main()
