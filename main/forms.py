from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'name',
                'type': 'text'
            }
        ),
        label="Имя"
    )
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'email',
                'type': 'email'
            }
        ),
        label="Почта"
    )
    login = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'login',
                'type': 'text'
            }
        ),
        label="Логин (телеграм\вк\номер телефона)"
    )
    text = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'text',
                'type': 'text'
            }
        ),
        label="Сообщение"
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'username',
                'id': 'username',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Логин"
    )
    password = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'password',
                'id': 'password',
                'type': 'password',
                'class': 'form-control'
            }
        ),
        label="Пароль"
    )



class ManagementCatalogForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'catalogName',
                'id': 'catalogName',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Название услуги"
    )
    price = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'currentPrice',
                'id': 'currentPrice',
                'type': 'number',
                'class': 'form-control'
            }
        ),
        label="Текущая цена"
    )
    old_price = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'oldPrice',
                'id': 'oldPrice',
                'type': 'number',
                'class': 'form-control'
            }
        ),
        label="Старая цена"
    )
    estimated_time = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'deadline',
                'id': 'deadline',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Сроки"
    )
    description = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'description',
                'id': 'description',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Описание"
    )



class ManagementWorksForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'catalogName',
                'id': 'catalogName',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Название работы"
    )
    image = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'workImage',
                'id': 'workImage',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Ссылка на изображение"
    )


class ManagementNewsForm(forms.Form):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'newTitle',
                'id': 'newTitle',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Заголовок"
    )
    description = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'newDescription',
                'id': 'newDescription',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Содержание"
    )

class ManagementDocumentsForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'documentName',
                'id': 'documentName',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Название документа (системное, как documentname)"
    )
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'documentTitle',
                'id': 'documentTItle',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Название документа"
    )
    content = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'documentContent',
                'id': 'documentContent',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Содержание документа"
    )


class ManagementReviewsForm(forms.Form):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'reviewName',
                'id': 'reviewName',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Имя пользователя"
    )
    estimation = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'reviewEstimation',
                'id': 'reviewEstimation',
                'type': 'number',
                'class': 'form-control'
            }
        ),
        label="Уровень оценка"
    )
    description = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'reviewDescription',
                'id': 'reviewDescription',
                'type': 'text',
                'class': 'form-control'
            }
        ),
        label="Отзыв"
    )