from django.shortcuts import redirect, render, reverse

from users.models import Questions, Tests


def tests(request, class_number, school):
    test = Tests.objects.filter(school__name=school, number_class__name=class_number)
    context = {'tests': test,
               'title': 'CheckYou - Список тестов',
               }
    return render(request, 'tests/tests.html', context)


def test_card(request, name, id):
    if request.method == 'POST':
        questions = Questions.objects.filter(test__id=id)
        print(type(questions))
        answers = []
        true_answers = []
        question_first_id = questions.first().id
        i = question_first_id
        print(question_first_id)
        print(questions.count())
        success = 0
        for item in range(question_first_id, question_first_id + questions.count()):
            answers.append(request.POST[f'{i}'])
            i += 1
        i = 0
        for item in questions:
            i += 1
            true_answers.append(item.true_answer)
        i = 0
        for answer, true_answer in zip(answers, true_answers):
            if answer == true_answer:
                success += 1

        print(answers)
        print(true_answers)
        print(success)

        url = reverse('tests:complete-test') + f'?success={success}'

        return redirect(url)

    else:
        questions = Questions.objects.filter(test__id=id)

        context = {'questions': questions,
                   'name': name,
                   'id': id,
                   'title': 'CheckYou - Тест',
                   }

        return render(request, 'tests/test-card.html', context)


def complete_test(request):
    success = request.GET.get('success')
    context = {'answers': success,
               'title': 'CheckYou - Завершение теста',}

    return render(request, 'tests/complete-test.html', context)
