from django.shortcuts import render
from .models import PHP, Python, JavaScript, Angular, Java, React, Django, Dot_Net, Node_JS


# Create your views here.
def Home(request):
    return render(request, 'Home.html')


def Python_Quiz(request):
    if request.method == 'POST':
        questions = Python.objects.all()
        wrong = 0
        correct = 0
        total = 0
        for question in questions:
            total = total + 1
            selected_answer = request.POST.get('selected_answers_{}'.format(question.id))
            if selected_answer == question.ans:
                correct = correct + 1
            else:
                wrong = wrong + 1
        score = correct / len(questions) * 100
        percentage = score / (total * 10) * 100
        context = {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'total': total,
            'percentage': percentage
        }
        return render(request, 'Python_Result.html', context)

    questions = Python.objects.all()
    context = {'questions': questions}
    return render(request, 'Python.html', context)


def Django_Quiz(request):
    if request.method == 'POST':
        questions = Django.objects.all()
        correct = 0
        wrong = 0
        total = 0
        for question in questions:
            total = total + 1
            selected_answers = request.POST.get('selected_answers_{}'.format(question.id))
            if selected_answers == question.ans:
                correct = correct + 1
            else:
                wrong = wrong + 1
        score = correct / len(questions) * 100
        percentage = score / (total * 10) * 100
        context = {'score': score,
                   'percentage': percentage,
                   'correct': correct,
                   'wrong': wrong,
                   'total': total}
        return render(request, 'Django_Result.html', context)
    questions = Django.objects.all()
    context = {
        'questions': questions}
    return render(request, 'Django.html', context)


def Angular_Quiz(request):
    if request.method == 'POST':
        questions = Angular.objects.all()
        correct = 0
        wrong =0
        total =0
        for question in questions:
            total = total+1
            selected_answers = request.POST.get('selected_answers_{}'.format(question.id))
            if selected_answers == question.ans:
                correct = correct+1
            else:
                wrong = wrong+1
        score = correct / len(questions)*100
        percentage = score/(total*10)*100
        context = {'score':score,
                   'percentage':percentage,
                   'correct':correct,
                   'wrong':wrong,
                   'total':total}
        return render(request,'Angular_Result.html',context)
    angular = Angular.objects.all()
    context = {'angular': angular}
    return render(request, 'Angular.html', context)


def PHP_Quiz(request):
    if request.method == 'POST':
        questions = PHP.objects.all()
        correct = 0
        wrong =0
        total =0
        for question in questions:
            total = total+1
            selected_answers = request.POST.get('selected_answers_{}'.format(question.id))
            if selected_answers == question.ans:
                correct = correct+1
            else:
                wrong = wrong+1
        score = correct / len(questions)*100
        percentage = score/(total*10)*100
        context = {'score':score,
                   'percentage':percentage,
                   'correct':correct,
                   'wrong':wrong,
                   'total':total}
        return render(request,'PHP_Result.html',context)
    php = PHP.objects.all()
    context = {
        'php': php
    }
    return render(request, 'PHP.html', context)


def Java_Quiz(request):
    if request.method == 'POST':
        questions = Java.objects.all()
        correct = 0
        wrong =0
        total =0
        for question in questions:
            total = total+1
            selected_answers = request.POST.get('selected_answers_{}'.format(question.id))
            if selected_answers == question.ans:
                correct = correct+1
            else:
                wrong = wrong+1
        score = correct / len(questions)*100
        percentage = score/(total*10)*100
        context = {'score':score,
                   'percentage':percentage,
                   'correct':correct,
                   'wrong':wrong,
                   'total':total}
        return render(request,'Java_Result.html',context)
    java = Java.objects.all()
    context = {
        'java': java
    }
    return render(request, 'Java.html', context)


def JavaScript_Quiz(request):
    if request.method == 'POST':
        questions = JavaScript.objects.all()
        correct = 0
        wrong =0
        total =0
        for question in questions:
            total = total+1
            selected_answers = request.POST.get('selected_answers_{}'.format(question.id))
            if selected_answers == question.ans:
                correct = correct+1
            else:
                wrong = wrong+1
        score = correct / len(questions)*100
        percentage = score/(total*10)*100
        context = {'score':score,
                   'percentage':percentage,
                   'correct':correct,
                   'wrong':wrong,
                   'total':total}
        return render(request,'JavaScript_Result.html',context)
    javascript = JavaScript.objects.all()
    context = {
        'javascript': javascript
    }
    return render(request, 'JavaScript.html', context)


def Dot_Net_Quiz(request):
    if request.method == 'POST':
        questions = Dot_Net.objects.all()
        correct = 0
        wrong =0
        total =0
        for question in questions:
            total = total+1
            selected_answers = request.POST.get('selected_answers_{}'.format(question.id))
            if selected_answers == question.ans:
                correct = correct+1
            else:
                wrong = wrong+1
        score = correct / len(questions)*100
        percentage = score/(total*10)*100
        context = {'score':score,
                   'percentage':percentage,
                   'correct':correct,
                   'wrong':wrong,
                   'total':total}
        return render(request,'Dot_Net_Result.html',context)
    dot_net = Dot_Net.objects.all()
    context = {
        'dot_net': dot_net
    }
    return render(request, 'Dot_Net.html', context)


def React_Quiz(request):
    if request.method == 'POST':
        questions = React.objects.all()
        correct = 0
        wrong =0
        total =0
        for question in questions:
            total = total+1
            selected_answers = request.POST.get('selected_answers_{}'.format(question.id))
            if selected_answers == question.ans:
                correct = correct+1
            else:
                wrong = wrong+1
        score = correct / len(questions)*100
        percentage = score/(total*10)*100
        context = {'score':score,
                   'percentage':percentage,
                   'correct':correct,
                   'wrong':wrong,
                   'total':total}
        return render(request,'React_Result.html',context)
    react = React.objects.all()
    context = {
        'react': react
    }
    return render(request, 'React.html', context)


def Node_Js_Quiz(request):
    if request.method == 'POST':
        questions = Node_JS.objects.all()
        correct = 0
        wrong =0
        total =0
        for question in questions:
            total = total+1
            selected_answers = request.POST.get('selected_answers_{}'.format(question.id))
            if selected_answers == question.ans:
                correct = correct+1
            else:
                wrong = wrong+1
        score = correct / len(questions)*100
        percentage = score/(total*10)*100
        context = {'score':score,
                   'percentage':percentage,
                   'correct':correct,
                   'wrong':wrong,
                   'total':total}
        return render(request,'NodeJs_Result.html',context)
    nodejs = Node_JS.objects.all()
    context = {
        'nodejs': nodejs
    }
    return render(request, 'Node_JS.html', context)
