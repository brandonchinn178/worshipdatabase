from django.test import TestCase
from django.db.utils import IntegrityError

from database.models import Song

class SongTest(TestCase):
    def test_no_title(self):
        """Every song MUST have a title"""
        self.assertRaises(
            IntegrityError,
            Song.objects.create
        )

    def test_default(self):
        song = Song.objects.create(title='test')
        self.assertEqual(song.title, 'test')
        self.assertEqual(song.artist, '')
        self.assertEqual(song.title_slug, '')
        self.assertEqual(song.speed, '')
        self.assertEqual(song.lyrics, None)
        self.assertEqual(song.doc, '')
        self.assertEqual(song.pdf, '')

    def test_slug(self):
        song = Song.objects.create(title='Test Title')
        self.assertEqual(song.title_slug, '')
        self.assertEqual(song.get_absolute_url(), '/database/test-title/')
        # calling get_absolute_url should set title_slug
        self.assertEqual(song.title_slug, 'test-title')

        song = Song.objects.create(title="Yet Another Test", title_slug="welll")
        # if has title_slug, nothing changes
        self.assertEqual(song.title_slug, 'welll')
        self.assertEqual(song.get_absolute_url(), '/database/welll/')
        self.assertEqual(song.title_slug, 'welll')