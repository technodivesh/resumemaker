from django.contrib import admin

from .models import UserProfile, Experience, Education, Skill, Project, AwardAchievement, CustomSection


# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ('guid', 'full_name', 'email', 'is_active', 'created_at', 'updated_at')
#     search_fields = ('full_name', 'email')


admin.site.register(UserProfile)
admin.site.register(Experience)
admin.site.register(Education)
# admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(AwardAchievement)
admin.site.register(CustomSection)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'user')  # Make sure these are real fields
    search_fields = ('name',)
    list_filter = ('proficiency', 'user')