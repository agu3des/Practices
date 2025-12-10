from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Livro

class Command(BaseCommand):
    help = 'Cria grupo de analistas de cadastro de produtos com permissões'

    def handle(self, *args, **options):
        # Obtem o ContentType do modelo Livro
        livro_content_type = ContentType.objects.get_for_model(Livro)

        # Cria o grupo "Analistas de Cadastro"
        group, created = Group.objects.get_or_create(name='Analistas de Cadastro')

        # Obtém as permissões para Livro
        add_permission = Permission.objects.get(
            codename='add_livro',
            content_type=livro_content_type
        )
        change_permission = Permission.objects.get(
            codename='change_livro',
            content_type=livro_content_type
        )
        delete_permission = Permission.objects.get(
            codename='delete_livro',
            content_type=livro_content_type
        )

        # Adiciona permissões ao grupo
        group.permissions.add(add_permission, change_permission, delete_permission)

        if created:
            self.stdout.write(self.style.SUCCESS('Grupo "Analistas de Cadastro" criado com sucesso!'))
        else:
            self.stdout.write(self.style.SUCCESS('Grupo "Analistas de Cadastro" já existe. Permissões atualizadas!'))