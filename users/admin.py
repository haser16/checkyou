from django.contrib import admin

from .models import Classes, Questions, Schools, Subject, Teacher, Tests, User

admin.site.register(Classes)
admin.site.register(Schools)
admin.site.register(Subject)
admin.site.register(Teacher)


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
    extra = 0


@admin.register(Tests)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'number_class', 'subject', 'teacher', )
    fields = (('school', 'number_class', 'name'), ('teacher', 'subject', 'image'))
    search_fields = ('name', 'subject', 'teacher', 'number_class', )
    inlines = [QuestionsInline, ]
    ordering = ('subject', )


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', )

