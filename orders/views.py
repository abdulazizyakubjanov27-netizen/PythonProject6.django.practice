from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm
from django.contrib.auth.decorators import login_required


# READ (list)
def order_list(request):
    order = Order.objects.all()
    print(order)
    return render(request, 'books/list.html', {'order': order})


@login_required
def book_create(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_list')

    return render(request, 'book/create.html', {'form': form})


@login_required
def book_update(request, pk):
    book = get_object_or_404(Order, pk=pk)
    form = OrderForm(request.POST or None, instance=order)

    if form.is_valid():
        form.save()
        return redirect('order_list')

    return render(request, 'book/update.html', {'form': form})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Order, pk=pk)

    if request.method == "Order":
        order.delete()
        return redirect('order_list')

    return render(request, 'order/delete.html', {'order': order})




