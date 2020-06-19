from django.test import TestCase
from bradoo.core.forms import ProductsModelForm, VendorsModelForm


class ProductsFormTest(TestCase):
    def test_form_has_fileds(self):
        """ Must have 4 fiels"""
        form = ProductsModelForm()
        expected = ['name', 'code', 'price', 'vendor']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_must_have_name(self):
        """Must have name"""
        form = self.make_validated_form(name='')
        self.assertTrue(form.errors)

    def test_must_have_code(self):
        """Must have name"""
        form = self.make_validated_form(code='')
        self.assertTrue(form.errors)       

    def make_validated_form(self, **kwargs):
        valid = dict(name='Leonardo Perrella', code='00000000000000',
                    price='Sao Caetano do Sul', vendor='Leonardo')
        data = dict(valid, **kwargs)
        form = VendorsModelForm(data)
        form.is_valid()
        return form


class VendorsFormTest(TestCase):
    
    def test_form_has_fileds(self):
        """ Must have 3 fiels"""
        form = VendorsModelForm()
        expected = ['name', 'cnpj', 'city']
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_cnpj_is_digit(self):
        """CNPJ must only accept numbers"""
        form = self.make_validated_form(cnpj='ABCD5678901')
        self.assertTrue(form.errors)
    
    def test_cpf_has_14_digits(self):
        """CNPJ must have 14 digits"""
        form = self.make_validated_form(cnpj='1234')
        self.assertTrue(form.errors)

    def test_must_have_name(self):
        """Must have name"""
        form = self.make_validated_form(name='')
        self.assertTrue(form.errors)

    def test_must_have_cnpj(self):
        """Must have cnpj"""
        form = self.make_validated_form(cnpj='')
        self.assertTrue(form.errors)
    
    def make_validated_form(self, **kwargs):
        valid = dict(name='Leonardo Perrella', cnpj='00000000000000',
                    city='Sao Caetano do Sul')
        data = dict(valid, **kwargs)
        form = VendorsModelForm(data)
        form.is_valid()
        return form
    