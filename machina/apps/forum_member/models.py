from machina.apps.forum_member.abstract_models import AbstractForumProfile
from machina.core.db.models import model_factory


ForumProfile = model_factory(AbstractForumProfile)
