from django.shortcuts import redirect, render, reverse

from users.models import Questions, Tests


def tests(request, class_number, school):
    test = Tests.objects.filter(school__name=school, number_class__name=class_number)
    context = {'tests': test}
    return render(request, 'tests/tests.html', context)


def test_card(request, name, id):
    if request.method == 'POST':
        questions = Questions.objects.filter(test__id=id)
        answers = []
        true_answers = []
        i = 0
        success = 0
        for item in questions:
            i += 1
            answers.append(request.POST[f'{i}'])
        i = 0
        for item in questions:
            i += 1
            true_answers.append(item.true_answer)
        i = 0
        for answer, true_answer in zip(answers, true_answers):
            if answer == true_answer:
                success += 1

        url = reverse('tests:complete-test') + f'?success={success}'

        return redirect(url)

    else:
        questions = Questions.objects.filter(test__id=id)

        context = {'questions': questions,
                   'name': name,
                   'id': id,
                   }

        return render(request, 'tests/test-card.html', context)


def complete_test(request):
    success = request.GET.get('success')
    context = {'answers': success}

    return render(request, 'tests/complete-test.html', context)
