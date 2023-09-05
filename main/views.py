from django.shortcuts import render, redirect, get_object_or_404
from funçõesprojeto import *
from . models import *
from django.contrib.auth.decorators import login_required
from funçõesprojeto import *
from . forms import *

# Renderizar as paginas 
def principal(request):
    return render(request, 'main/index.html')

def contato(request):
    return render(request, 'main/contato.html')

def pagina_inicial(request):
    return render(request, 'main/index.html')

@login_required # Solicita login para as informações do sistema
def area_restrita(request):
    return render(request,'main/area_restrita.html')

def cadastrar_pessoa(request):
    return render(request, 'main/cadastro_pessoa.html')

def cadastrar_funcao(request):
    return render(request, 'main/cadastro_funcao.html')

def atualizacao(request):
    return render(request, 'main/atualizacoes.html')

def atualizacao_realizada(request):
    return render(request, 'main/atualizacao_realizada.html')

def cadastro_realizado(request):
    return render(request, 'main/cadastro_realizado.html')

def mapa(request):
    return render(request, 'main/mapa.html')

def cadastrar(request): # Função de cadastro
    if request.method == 'POST':
            nome = request.POST.get('nome_cadastro')
            dn = request.POST.get('data_nascimento')
            rg = request.POST.get('rg')
            cpf = request.POST.get('cpf')
            idade = request.POST.get('idade')
            end = request.POST.get('endereco')
            tel = request.POST.get('telefone')
            nat = request.POST.get('naturalidade')
            esc = request.POST.get('escolaridade')
            renda = request.POST.get('renda')
            ec = request.POST.get('estado_civil')
            nis = request.POST.get('nis')

            cadastro(nome, dn, rg, cpf, idade, end, tel, nat, esc, renda, ec, nis)

            
        
            if cadastro(nome, dn, rg, cpf, idade, end, tel, nat, esc, renda, ec, nis) == False: # Se o cadastro não for válido a pagina atualiza
                mensagem = 'Cadastro Inválido'
                return render(request, 'main/cadastro_pessoa.html', {'mensagem': mensagem})
        
    return render(request, 'main/cadastro_pessoa.html')

def foto(request): # Função de anexar foto a um cadastrado
    query = Cadastrados.objects.all() # Buscar o nome dos cadastrados
    if request.method == 'POST':
        form = Foto_Form(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('/')
        print(form)
        
    else:
        form = Foto_Form()

    return render(request, 'main/foto.html', {'form': form, 'query': query} )

def add_trabalhos(request): # Função pra adicionar trabalho ao banco
    if request.method == 'POST':
        trab = request.POST.get('add_trabalho')
        add_trabalho(trab)

    return render(request, 'main/cadastro_funcao.html')

def definir_empregados(request): # Determinar trabalho para pessoas cadatradas
    if request.method == 'POST':
        nome = request.POST.get('nome_empregado')
        id_servico = request.POST.get('id_serviço')
        id_pessoa = request.POST.get('id_pessoa')

        designar_trabalho(nome, id_servico, id_pessoa)

def delete_cadastrado(request): # Função de deletar pessoas cadastradas
    if request.method == 'POST':
        id = request.POST.get('id_del')

        delete(id)
    
def delete_serv(request): # Função de deletar trabalhos cadastrados
    if request.method == 'POST':
        id = request.POST.get('id_del_serv')

        delete_serv(id)
    
    return render

def cnpj(request): # Função de Cadastro de Empresas
    mensagem = None
    dic_dados = {}

    if request.method == 'POST':
        if 'pesquisar' in request.POST:
            cnpj = request.POST.get('cnpj')
            if cnpj == "":
                mensagem = "CNPJ não encontrado"
            else:
                dados = consult_cnpj(cnpj) 
                if dados.get('cnpj') is not None: # Verifica se o CNPJ existe
                    cnpj = dados.get('cnpj')
                    nome = dados.get('fantasia')
                    local = dados.get('logradouro')
                    tel = dados.get('telefone')
                    email = dados.get('email')

                    # Cria um dicionario com os Dados da empresa: CNPJ, Nome da empresa, Logradouro, Telefone e Email 
                    dic_dados = {
                        'cnpj': cnpj,
                        'nome': nome,
                        'local': local,
                        'tel': tel,
                        'email': email
                    }
                else:
                    mensagem = "CNPJ não encontrado"
        
        # Salva as informações da Empresa no banco de dados
        elif 'enviar' in request.POST:
            # Processar o formulário enviado aqui
            # Você pode acessar os campos diretamente em request.POST

            cnpj = request.POST.get('cnpj')
            nome = request.POST.get('nome')
            local = request.POST.get('local')
            tel = request.POST.get('tel')
            email = request.POST.get('email')

            novo_registro = Empresas(cnpj=cnpj, nome=nome, endereço=local, telefone=tel, email=email)
            novo_registro.save()

            # Fazer o que você precisa com esses dados aqui
            
            pass

    return render(request, 'main/consulta_cnpj.html', {'dic_dados': dic_dados, 'mensagem': mensagem})
    

def contato(request): #Função de contado com o Sistema
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('msg')

        add_contato(nome, email, mensagem) 

    return render(request, 'main/contato.html')
    
def atualizar_funcao(request): # Chama os trabalhos cadastrados no banco para o Frontend
    query = Servios.objects.all().values_list('serviços')
    lista = []

    for i in query:
        i = str(i[0])
        lista.append(i)

    return render(request, 'main/atualizar_funcao.html', {'query':lista})

def atualizar_funcao_id(request, id): # Função de atualização de trabalhos já cadastrados
    query = get_object_or_404(Servios, serviços=id)
    form = ServicoForm(instance=query)
    if (request.method=='POST'):
        form = ServicoForm(request.POST, instance=query)
        if form.is_valid():
            query.save()
            return redirect('/atualizacao_realizada')
        else:
            return render(request, 'main/atualizar_funcao_id.html', {'form':form, 'query':query})
        
    else:

        return render(request, 'main/atualizar_funcao_id.html',  {'form':form, 'query':query})
    
def atualizar_cadastro(request): # Chama os cadastros de pessoas para o Frontend
    query = Cadastrados.objects.all().values_list('nome')
    lista = []

    for i in query:
        i = str(i[0])
        lista.append(i)

    return render(request, 'main/atualizar_pessoas.html', {'query':lista})

def atualizar_cadastro_id(request, id): # Atualiza as informações das pessoas já cadastradas no Sistema
    query = get_object_or_404(Cadastrados, nome=id)
    form = CadastroForm(instance=query)
    if (request.method=='POST'):
        form = CadastroForm(request.POST, instance=query)
        if form.is_valid():
            query.save()
            return redirect('/atualizacao_realizada')
        else:
            return render(request, 'main/atualizar_pessoas_id.html', {'form':form, 'query':query})
    else:
        return render(request, 'main/atualizar_pessoas_id.html',  {'form':form, 'query':query})