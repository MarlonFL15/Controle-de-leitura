from django.contrib.auth.base_user import BaseUserManager


class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome= None, pais_origem = None, password = None):
        if not email:
            raise ValueError('O usuário precisa de um email')
        usuario = self.model(
            nome = nome,
            email = self.normalize_email(email),
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, nome, email, password):
        usuario = self.create_user(
            email = email,
            nome = nome,
        )
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.set_password(password)
        usuario.save()
        return usuario