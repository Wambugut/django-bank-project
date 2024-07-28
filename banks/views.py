from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Bank, Branch
from django.http import JsonResponse

@login_required
def add_bank(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        inst_num = request.POST.get('inst_num')
        swift_code = request.POST.get('swift_code')

        if not all([name, description, inst_num, swift_code]):
            return render(request, 'banks/add_bank.html', {'error': "This field is required"})

        Bank.objects.create(
            name=name,
            description=description,
            institution_number=inst_num,
            swift_code=swift_code,
            owner=request.user
        )
        return redirect('/banks/')

    return render(request, 'banks/add_bank.html')

@login_required
def add_branch(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        transit_num = request.POST.get('transit_num')
        address = request.POST.get('address')
        email = request.POST.get('email')
        capacity = request.POST.get('capacity')
        bank_id = request.POST.get('bank_id')

        if not all([name, transit_num, address, email, bank_id]):
            return render(request, 'banks/add_branch.html', {'error': "This field is required"})

        bank = get_object_or_404(Bank, id=bank_id)
        Branch.objects.create(
            name=name,
            transit_number=transit_num,
            address=address,
            email=email,
            capacity=capacity,
            bank=bank
        )
        return redirect(f'/banks/{bank.id}/details/')

    banks = Bank.objects.all()
    return render(request, 'banks/add_branch.html', {'banks': banks})

def list_all_banks(request):
    banks = Bank.objects.all()
    return render(request, 'banks/list_banks.html', {'banks': banks})

def bank_details(request, bank_id):
    bank = get_object_or_404(Bank, id=bank_id)
    branches = bank.branches.all()
    return render(request, 'banks/bank_details.html', {'bank': bank, 'branches': branches})

def branch_details(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    return JsonResponse({
        'name': branch.name,
        'transit_number': branch.transit_number,
        'address': branch.address,
        'email': branch.email,
        'capacity': branch.capacity,
        'last_modified': branch.last_modified
    })