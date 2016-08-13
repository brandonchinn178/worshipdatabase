from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.template.loader import render_to_string
from django.conf import settings

import facebook, os

from database.models import Song

@receiver(post_save, sender=Song)
def post_to_facebook(sender, instance, created, **kwargs):
    """
    When a Song is added to the database, post to Facebook automatically.
    """
    if created and settings.IS_HEROKU:
        access_token = os.environ.get('FACEBOOK_ACCESS_TOKEN')
        context = {
            'song': instance
        }
        message = render_to_string('facebook_post.txt', context).strip()
        graph = facebook.GraphAPI(access_token=access_token)
        try:
            graph.put_object('me', 'feed', message=message)
        except Exception as e:
            import logging
            logging.error('An error occurred when posting to Facebook: %s' % e)
            logging.debug('The message: %s' % message)
            raise e # re-raise exception to alert user something went wrong
