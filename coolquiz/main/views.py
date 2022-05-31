from select import select
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Quiz, QuizQuestion, QuizAnswer, TakeAnswer, Take


def index(request):
    quizzes = Quiz.objects.order_by("-created_at")
    context = {
        'quizzes': quizzes,
        'user': '',
    }
    if request.user.is_authenticated:
        context["user"] = request.user.username
    return render(request, 'main/index.html', context)


def get_quiz_context(request, quiz_slug):
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    questions = QuizQuestion.objects.filter(quiz_id=quiz.id)
    answers = QuizAnswer.objects.filter(quiz_id=quiz.id)
    context = {
        'quiz': quiz,
        'questions': questions,
        'answers': answers,
        'user': request.user,
    }
    return context


def display_quiz(request, quiz_slug):
    if not request.user.is_authenticated:
        return redirect('login_page')
    context = get_quiz_context(request, quiz_slug)
    return render(request, 'main/quiz.html', context)


def display_result(request, quiz_slug, username):
    context = get_quiz_context(request, quiz_slug)
    take = Take.objects.create(
        user_id = context['user'],
        quiz_id = context['quiz'],
    )
    score = 0
    total = 0
    for ques in context['questions'].iterator():
        total += 1
        answer_id = request.POST.get(str(ques.id))
        answer = QuizAnswer.objects.filter(pk=answer_id)
        if answer[0].correct:
            score += 1
        take_answer = TakeAnswer.objects.create(
            take_id = take,
            answer_id = answer[0],
            question_id = ques
        )
    context["user_score"] = score
    context["total_score"] = total
    context["percent_efficiency"] = int(score / (total / 100))
    context["questions"] = zip(context["questions"], TakeAnswer.objects.filter(take_id=take.id))
    take.user_score = score
    take.total_score = total
    take.percent_efficiency = context["percent_efficiency"]
    take.save()

    return render(request, 'main/result.html', context)
