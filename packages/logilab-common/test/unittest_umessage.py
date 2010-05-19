# encoding: iso-8859-15

from logilab.common.testlib import TestCase, unittest_main
from logilab.common.umessage import UMessage, decode_QP

import email

class UMessageTC(TestCase):

    def setUp(self):
        msg1 = email.message_from_file(open('data/test1.msg'))
        self.umessage1 = UMessage(msg1)
        msg2 = email.message_from_file(open('data/test2.msg'))
        self.umessage2 = UMessage(msg2)

    def test_get_subject(self):
        subj = self.umessage2.get('Subject')
        self.assertEquals(type(subj), unicode)
        self.assertEquals(subj, u'À LA MER')

    def test_get_all(self):
        to = self.umessage2.get_all('To')
        self.assertEquals(type(to[0]), unicode)
        self.assertEquals(to, [u'élément à accents <alf@logilab.fr>'])

    def test_get_payload_no_multi(self):
        payload = self.umessage1.get_payload()
        self.assertEquals(type(payload), unicode)

    def test_decode_QP(self):
        test_line =  '=??b?UmFwaGHrbA==?= DUPONT<raphael.dupont@societe.fr>'
        test = decode_QP(test_line)
        self.assertEquals(type(test), unicode)
        self.assertEquals(test, u'Raphaël DUPONT<raphael.dupont@societe.fr>')


if __name__ == '__main__':
    unittest_main()
