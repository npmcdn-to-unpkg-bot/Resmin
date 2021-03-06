from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

from apps.question.models import QuestionMeta

from resmin.utils import _set_avatar_to_answer


class Command(BaseCommand):
    def handle(self, *args, **options):
        for user in User.objects.all():
            qm = QuestionMeta.objects.get(id=settings.AVATAR_QUESTIONMETA_ID)
            story = user.story_set.filter(question_meta=qm).first()
            if story:
                _set_avatar_to_answer(story)
                print "avatar fixed for %s" % story.owner
