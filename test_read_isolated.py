import unittest
from unittest.mock import patch
from read_excel_isolated import read_email_data


class TestRead(unittest.TestCase):

  sample_emails = {
    "email": ['h@dummy.com', 'q@dummy.com'],
    "hike": ['10%', '20%']
  }

  @patch('read_excel_isolated.pandas.read_excel', return_value=sample_emails)
  def test_email_read_from_file(self, _):
    mails = read_email_data()
    self.assertEqual(len(mails), len(TestRead.sample_emails["email"]))

  @patch('read_excel_isolated.pandas.read_excel', side_effect=IOError())
  def test_error_report_on_non_existent_file(self, _):
    mails = read_email_data()
    self.assertEqual(len(mails), 0)


if __name__ == '__main__':
  unittest.main()
