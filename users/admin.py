from django.contrib import admin

from .models import Classes, Questions, Schools, Subject, Teacher, Tests, User

admin.site.register(User)
admin.site.register(Classes)
admin.site.register(Schools)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Questions)


class SchoolInline(admin.TabularInline):
    fk_name = 'Schools'
    model = Schools


class ClassesInline(admin.TabularInline):
    fk_name = 'Classes'
    model = Classes


class QuestionsInline(admin.TabularInline):
    fk_name = 'test'
    model = Questions
    inlines = [Schools, Classes]


@admin.register(Tests)
class ProductsAdmin(admin.ModelAdmin):
    fields = (('school', 'number_class', 'name'), ('teacher', 'subject', 'image'))
    inlines = [QuestionsInline, ]
