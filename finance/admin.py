from django.contrib import admin
from .models import Finance


class FinanceAdmin(admin.ModelAdmin):
    fields = ['name', 'amount', 'date', 'slug', 'finance_type']
    prepopulated_fields = {'slug': ('name', )}

# class IncomeAdmin(admin.ModelAdmin):
#     fields = ['amount', 'pay_date']
#     prepopulated_fields = {'slug': ('name', )}

# class DebtAdmin(admin.ModelAdmin):
#     fields = ['amount', 'due_date']
#     prepopulated_fields = {'slug': ('name', )}

# class ExpenseAdmin(admin.ModelAdmin):
#     fields = ['amount', 'description']
#     prepopulated_fields = {'slug': ('name', )}

# admin.site.register(Income, IncomeAdmin)
# admin.site.register(Debt, DebtAdmin)
# admin.site.register(Expense, ExpenseAdmin)

admin.site.register(Finance, FinanceAdmin)