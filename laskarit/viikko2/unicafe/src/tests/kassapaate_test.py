from kassapaate import Kassapaate
from maksukortti import Maksukortti
import unittest

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_tiedot_oikein_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_edullisesti_toimii_kun_maksu_on_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500),260)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_syo_maukkaasti_toimii_kun_maksu_on_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500),100)
        self.assertEqual(self.kassapaate.maukkaat,1)
    
    def test_syo_edullisesti_toimii_oikein_kun_maksu_ei_ole_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(10),10)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_syo_maukkaasti_toimii_oikein_kun_maksu_ei_ole_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(20),20)
        self.assertEqual(self.kassapaate.maukkaat,0)
    
    def test_syo_edullisesti_toimii_oikein_jos_kortilla_on_tarpeeksi_rahaa(self):
        kortti = Maksukortti(1000)
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,1)
    
    def test_myytyjen_lounaiden_maara_kasvaa_jos_maksu_on_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat,1)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_syo_maukkaasti_toimii_oikein_jos_kortilla_on_tarpeeksi_rahaa(self):
        kortti = Maksukortti(1000)
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,1)
    
    def test_syo_edullisesti_toimii_oikein_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        kortti = Maksukortti(1)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(kortti))
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)
    
    def test_syo_maukkaasti_toimii_oikein_jos_kortilla_ei_ole_tarpeeksi_rahaa(self):
        kortti = Maksukortti(1)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(kortti))
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,0)
    
    def test_kortille_lataaminen_toimii(self):
        kortti = Maksukortti(1)
        self.kassapaate.lataa_rahaa_kortille(kortti,2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa,102000)
        self.assertEqual(kortti.saldo,2001)

    def test_kortille_ei_voi_lataa_negatiivinen_maara(self):
        kortti = Maksukortti(1)
        self.kassapaate.lataa_rahaa_kortille(kortti,-20)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(kortti.saldo,1)

