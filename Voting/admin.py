from django.contrib import admin
from Voting.models import *
from django.utils.translation import gettext as _


class VoteItemInline(admin.TabularInline):
    model = Item
    extra = 0
    max_num = 15


class VoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'vote_count', 'is_published')
    inlines = [VoteItemInline, ]


admin.site.register(Poll, VoteAdmin)
