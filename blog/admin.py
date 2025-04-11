import openpyxl
from openpyxl import Workbook
from io import BytesIO
from django.http import HttpResponse
from django.contrib import admin
from .models import PatientData
from datetime import datetime


@admin.register(PatientData)
class PatientDataAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'name', 'date_of_birth', 'gender')
    actions = ["export_as_excel"]

    @admin.action(description="Export selected patients to Excel")
    def export_as_excel(self, request, queryset):
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Patient Data"

        field_names = [field.verbose_name or field.name for field in PatientData._meta.fields]
        field_keys = [field.name for field in PatientData._meta.fields]

        worksheet.append(field_names)

        for obj in queryset:
            row = []
            for field in field_keys:
                value = getattr(obj, field)

                # Agar datetime bo‘lsa va tzinfo bor bo‘lsa — uni naive datetime ga aylantirish
                if isinstance(value, datetime) and value.tzinfo is not None:
                    value = value.replace(tzinfo=None)

                row.append(value)
            worksheet.append(row)

        output = BytesIO()
        workbook.save(output)
        output.seek(0)

        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=patient_data.xlsx'
        return response
