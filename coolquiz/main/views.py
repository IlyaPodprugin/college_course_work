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


def display_quiz(request, quiz_slug):
    if not request.user.is_authenticated:
        return redirect('login_page')
    quiz = get_object_or_404(Quiz, slug=quiz_slug)
    questions = QuizQuestion.objects.filter(quiz_id=quiz.id)
    answers = QuizAnswer.objects.filter(quiz_id=quiz.id)
    context = {
        'quiz': quiz,
        'questions': questions,
        'answers': answers,
        'user': '',
    }
    if request.user.is_authenticated:
        context["user"] = request.user.username
    if request.method == 'POST':
        print(request.POST)
        score = 0
        total = 0
        for ques in questions.iterator():
            total += 1
            answer_id = request.POST.get(str(ques.id))
            answer = QuizAnswer.objects.filter(pk=answer_id)
            if answer[0].correct:
                score += 1
        context["score"] = score
        context["total"] = total
        return render(request, 'main/result.html', context)
    return render(request, 'main/quiz.html', context)

