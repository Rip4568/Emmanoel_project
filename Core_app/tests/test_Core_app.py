
class TesteClass():
	def test_primeiro_teste(self):
		assert True

	def test_importacao_do_perfil(self):
		import django
		django.setup()
		from Perfil_app.models import Perfil

	""" def test_valor_nulo_do_nickname_ao_ser_criado():
		from ...Perfil_app.models import Perfil
		assert Perfil.objects.create().nick_name == '' """