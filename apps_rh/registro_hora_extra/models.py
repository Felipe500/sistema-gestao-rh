
from django.db import models
from django.urls import reverse
from django.core.mail import send_mail, mail_admins, send_mass_mail
from apps_rh.funcionario.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    utilizada = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(RegistroHoraExtra, self).save(*args, **kwargs)
        #data = {'cliente': self.first_name}
        mensagem_email = ('Feita a alteração no funcionario: '+self.funcionario.nome)
        send_mail(
            'Novo cliente cadastrado',
            mensagem_email,
            'suporte@felipebrxdev.xyz',
            ['felipe.brx.dev@gmail.com'],
            html_message=  '<html>html body</html>',
            fail_silently=False,
        )



    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.funcionario.id])

    def __str__(self):
        return self.motivo
