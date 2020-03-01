import unittest
from datetime import datetime


from pnp_datetime.pnp_datetime import Pnp_Datetime

class TestPnpDatetime(unittest.TestCase):

    def test_datetime_to_string_iso8601_sepT(self):
        """
        test convert convert from datetime to string, sperator is 'T'
        """
        expect_value = "2018-06-19T06:48:25.699000+00:00"
        dt_dt = datetime.strptime(expect_value, "%Y-%m-%dT%H:%M:%S.%f%z")
        test_value = Pnp_Datetime.datetime_to_str(dt_dt)
        self.assertEqual(expect_value, test_value)


    def test_datetime_to_string_iso8601_sepSpace(self):
        """
        test convert convert from datetime to string, sperator is ' '
        """
        expect_value  = "2018-06-19 06:48:25.699000+00:00"
        dt_dt = datetime.strptime(expect_value , "%Y-%m-%d %H:%M:%S.%f%z")
        test_value = Pnp_Datetime.datetime_to_str(dt_dt, sep=' ')
        self.assertEqual(expect_value, test_value)

    def test_string_to_datetime_to_string_sepT(self):
        """
        test convert string to datetime, and then convert from datetime to string
        """
        expect_value = "2018-06-19T06:48:25.699000+00:00"
        dt_dt = Pnp_Datetime.str_to_datetime(expect_value)
        test_value = Pnp_Datetime.datetime_to_str(dt_dt)

        self.assertEqual(expect_value, test_value)

    def test_string_to_datetime_to_string_pattern11_1(self):
        """
        test convert string to datetime, 2001-01-01T05:28:22.198+00:00
        """
        str_dt = "2001-01-01T05:28:22.198+00:00"
        expect_value = datetime.strptime(str_dt, "%Y-%m-%dT%H:%M:%S.%f%z")
        test_value = Pnp_Datetime.str_to_datetime(str_dt)

        self.assertEqual(expect_value, test_value)

    def test_string_to_datetime_to_string_pattern11_2(self):
        """
        test convert string to datetime, 2001-01-01T05:28:22.198+0000
        """
        str_dt = "2001-01-01T05:28:22.198+0000"
        expect_value = datetime.strptime(str_dt, "%Y-%m-%dT%H:%M:%S.%f%z")
        test_value = Pnp_Datetime.str_to_datetime(str_dt)

        self.assertEqual(expect_value, test_value)



    def test_string_to_datetime_to_string_pattern21_1(self):
        """
        test convert string to datetime, 2001-01-01T05:28:22+00:00
        """
        str_dt = "2001-01-01T05:28:22+00:00"
        expect_value = datetime.strptime(str_dt, "%Y-%m-%dT%H:%M:%S%z")
        test_value = Pnp_Datetime.str_to_datetime(str_dt)

        self.assertEqual(expect_value, test_value)


    def test_string_to_datetime_to_string_pattern21_2(self):
        """
        test convert string to datetime, 2001-01-01T05:28:22+0000
        """
        str_dt = "2001-01-01T05:28:22+0000"
        expect_value = datetime.strptime(str_dt, "%Y-%m-%dT%H:%M:%S%z")
        test_value = Pnp_Datetime.str_to_datetime(str_dt)

        self.assertEqual(expect_value, test_value)




    def test_string_to_datetime_to_string_pattern22_1(self):
        """
        test convert string to datetime, 2001-01-01 05:28:22+00:00
        """
        str_dt = "2001-01-01 05:28:22+00:00"
        expect_value = datetime.strptime(str_dt, "%Y-%m-%d %H:%M:%S%z")
        test_value = Pnp_Datetime.str_to_datetime(str_dt)

        self.assertEqual(expect_value, test_value)


    def test_string_to_datetime_to_string_pattern22_2(self):
        """
        test convert string to datetime, 2001-01-01 05:28:22+0000
        """
        str_dt = "2001-01-01 05:28:22+0000"
        expect_value = datetime.strptime(str_dt, "%Y-%m-%d %H:%M:%S%z")
        test_value = Pnp_Datetime.str_to_datetime(str_dt)

        self.assertEqual(expect_value, test_value)



    def test_string_to_datetime_to_string_pattern31_1(self):
        """
        test convert string to datetime, 2001-01-01T16:41:24Z
        """
        str_dt = "2001-01-01T16:41:24Z"
        expect_value = datetime.strptime(str_dt, "%Y-%m-%dT%H:%M:%S%z")
        test_value = Pnp_Datetime.str_to_datetime(str_dt)

        self.assertEqual(expect_value, test_value)


    def test_string_to_datetime_to_string_pattern31_2(self):
        """
        test convert string to datetime, 2001-01-01 16:41:24Z
        """
        str_dt = "2001-01-01 16:41:24Z"
        expect_value = datetime.strptime(str_dt, "%Y-%m-%d %H:%M:%S%z")
        test_value = Pnp_Datetime.str_to_datetime(str_dt)

        self.assertEqual(expect_value, test_value)



    def test_datetime_to_string_to_datetime_sepT(self):
        """
        test convert datetime to string, and then convert from string to datetime 
        """
        expect_value = Pnp_Datetime.utcnow()
        str_dt = Pnp_Datetime.datetime_to_str(expect_value)
        test_value = Pnp_Datetime.str_to_datetime(str_dt)
        self.assertEqual(expect_value, test_value)


    def test_datetime_to_string_utcnow(self):
        """
        test convert datetime to string, and then convert from string to datetime 
        """
        utc_now = datetime.utcnow()
        expect_value = datetime.strftime(utc_now, "%Y-%m-%dT%H:%M:%S.%f%z")
        test_value = Pnp_Datetime.datetime_to_str(utc_now)
        self.assertEqual(expect_value, test_value)


    def test_now_of_tz(self):
        """
        test now of given timezone 
        """
        utc_now_1 = Pnp_Datetime.utcnow()
        tz_now = Pnp_Datetime.now_of_tz("Australia/Sydney")
        utc_now_2 = Pnp_Datetime.utcnow()
        self.assertTrue(utc_now_1 <= tz_now <= utc_now_2)

    def test_datetime_plus_months(self):
        """
        test datetime_plus_months
        """

        str_dt_0 = "2001-01-31T06:28:22.199000+00:00"
        str_dt_1 = "2001-02-28T06:28:22.199000+00:00"   # +1 month
        str_dt_2 = "2002-04-30T06:28:22.199000+00:00"   # +15 months

        dt_0 = Pnp_Datetime.str_to_datetime(str_dt_0)
        dt_1 = Pnp_Datetime.str_to_datetime(str_dt_1)
        dt_2 = Pnp_Datetime.str_to_datetime(str_dt_2)

        result_dt_1 = Pnp_Datetime.datetime_plus_months(dt_0, 1)
        result_dt_2 = Pnp_Datetime.datetime_plus_months(dt_0, 15)

        self.assertTrue((dt_1 == result_dt_1) and (dt_2 == result_dt_2))
        

    def test_datetime_minus_months(self):
        """
        test datetime_plus_months
        """

        str_dt_0 = "2002-04-30T06:28:22.199000+00:00"   
        str_dt_1 = "2002-03-30T06:28:22.199000+00:00"   # -1 month
        str_dt_2 = "2001-04-30T06:28:22.199000+00:00"   # -12 month
        str_dt_3 = "2001-01-30T06:28:22.199000+00:00"   # -15 month

        dt_0 = Pnp_Datetime.str_to_datetime(str_dt_0)
        dt_1 = Pnp_Datetime.str_to_datetime(str_dt_1)
        dt_2 = Pnp_Datetime.str_to_datetime(str_dt_2)
        dt_3 = Pnp_Datetime.str_to_datetime(str_dt_3)

        result_dt_1 = Pnp_Datetime.datetime_minus_months(dt_0, 1)
        result_dt_2 = Pnp_Datetime.datetime_minus_months(dt_0, 12)
        result_dt_3 = Pnp_Datetime.datetime_minus_months(dt_0, 15)

        self.assertTrue((dt_1 == result_dt_1) and (dt_2 == result_dt_2) and (dt_3 == result_dt_3))
        

    def test_datetime_plus(self):
        """
        test datetime_plus
        """
        str_dt_0 = "2002-04-30T06:28:22.199000+00:00"   
        str_dt_1 = "2004-05-01T06:28:22.199000+00:00"   # +1 year, +12 month, +1 day
        str_dt_2 = "2003-06-09T06:28:22.199000+00:00"   # +1 year, +40 day

        dt_0 = Pnp_Datetime.str_to_datetime(str_dt_0)
        dt_1 = Pnp_Datetime.str_to_datetime(str_dt_1)
        dt_2 = Pnp_Datetime.str_to_datetime(str_dt_2)

        result_dt_1 = Pnp_Datetime.datetime_plus(dt_0, years=1, months=12, days=1)
        result_dt_2 = Pnp_Datetime.datetime_plus(dt_0, years=1, months=0, days=40)
        #self.assertTrue((dt_1 == result_dt_1) and (dt_2 == result_dt_2) and (dt_3 == result_dt_3))
        self.assertTrue((dt_1 == result_dt_1) and (dt_2 == result_dt_2)) 


    def test_datetime_minus(self):
        """
        test datetime_minus
        """
        str_dt_0 = "2003-06-09T06:28:22.199000+00:00"   
        str_dt_1 = "2002-05-31T06:28:22.199000+00:00"   # -12 month, -9 day
        str_dt_2 = "2002-04-30T06:28:22.199000+00:00"   # -1 year, -40 days

        dt_0 = Pnp_Datetime.str_to_datetime(str_dt_0)
        dt_1 = Pnp_Datetime.str_to_datetime(str_dt_1)
        dt_2 = Pnp_Datetime.str_to_datetime(str_dt_2)

        result_dt_1 = Pnp_Datetime.datetime_minus(dt_0, years=0, months=12, days=9)
        result_dt_2 = Pnp_Datetime.datetime_minus(dt_0, years=1, months=0, days=40)
        #self.assertTrue((dt_1 == result_dt_1) and (dt_2 == result_dt_2) and (dt_3 == result_dt_3))
        self.assertTrue((dt_1 == result_dt_1) and (dt_2 == result_dt_2)) 


    def test_local_current_month_begin_time(self):
        """
        """
        result_1 = Pnp_Datetime.local_current_month_begin_time()
        print("local current_month_begin time: {}".format(result_1))
        self.assertTrue(True)
        

    def test_local_timezone_offset_seconds(self):
        """
        """
        result_1 = Pnp_Datetime.local_timezone_offset_seconds()
        print("local timezone offset seconds: {}, hour:{}".format(result_1, result_1/3600))
        self.assertTrue(True)


    def test_local_now(self):
        """
        """
        result_1 = Pnp_Datetime.local_now()
        print("local now: {}".format(result_1))
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
