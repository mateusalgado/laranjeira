import streamlit as st

# Simulação de um banco de dados de usuários
user_db = {
    "admin": {"password": "admin123", "name": "Administrador"}
}

# Função para verificar o login
def login(username, password):
    if username in user_db and user_db[username]["password"] == password:
        return True
    return False

# Inicializando o estado da sessão
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'register_step' not in st.session_state:
    st.session_state.register_step = 1  # Controla a etapa do cadastro

# Página principal com etapas de registro
if st.session_state.logged_in:
    st.sidebar.title("Menu")
    st.sidebar.write(f"Usuário: {st.session_state.name}")

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.name = ""
        st.rerun()

else:
    auth_mode = st.experimental_get_query_params().get("mode", ["login"])[0]

    if auth_mode == "login":
        st.image("logo.png", use_column_width=True)

        st.write("# Login")
        username = st.text_input("Usuário")
        password = st.text_input("Senha", type="password")

        col1, col2 = st.columns(2)

        with col1:
            login_button = st.button("Login", use_container_width=True)

        with col2:
            register_button = st.button("Registrar-se agora", use_container_width=True)

        st.markdown("[Esqueci a senha](?mode=forgot_password)")

        if login_button:
            if login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.name = user_db[username]["name"]
                st.success("Login bem-sucedido!")
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos!")

        if register_button:
            st.experimental_set_query_params(mode="register")

    elif auth_mode == "register":
        if st.session_state.register_step == 1:
            with st.form("business_info_form"):
                st.write("# Cadastro - Etapa 1/3")
                st.subheader("📊 Informações Empresariais")

                cnpj = st.text_input("CNPJ")
                col1, col2 = st.columns(2)
                nome_fantasia = col1.text_input("Nome Fantasia")
                razao_social = col2.text_input("Razão Social")

                cep = st.text_input("CEP")
                col3, col4 = st.columns(2)
                rua = col3.text_input("Rua")
                numero = col4.text_input("Número")

                complemento = st.text_input("Complemento")
                bairro = st.text_input("Bairro")

                col5, col6 = st.columns(2)
                cidade = col5.text_input("Cidade")
                estado = col6.text_input("Estado")

                submit_button = st.form_submit_button(label="Continuar", use_container_width=True)

            if submit_button:
                st.session_state.register_step = 2
                st.rerun()

        elif st.session_state.register_step == 2:
            with st.form("documents_form"):
                st.write("# Cadastro - Etapa 2/3")
                st.subheader("Documentos Importantes")
                contrato_social = st.file_uploader("Foto do contrato social")
                cnpj_photo = st.file_uploader("Enviar foto do cartão CNPJ")
                rg_frontal = st.file_uploader("Foto frontal do RG do responsável")
                rg_verso = st.file_uploader("Foto do verso do RG do responsável")
                selfie_rg = st.file_uploader("Selfie segurando o RG do responsável")

                submit_button2 = st.form_submit_button(label="Continuar", use_container_width=True)

            if submit_button2:
                st.session_state.register_step = 3
                st.rerun()

        elif st.session_state.register_step == 3:
            with st.form("account_form"):
                st.write("# Cadastro - Etapa 3/3")
                st.subheader("Os últimos dados para finalizar o contrato")

                username = st.text_input("Username")
                email = st.text_input("E-mail")
                col1, col2 = st.columns(2)
                senha = col1.text_input("Senha", type="password")
                confirmar_senha = col2.text_input("Confirmar Senha", type="password")
                faturamento_medio_mensal = st.text_input("Faturamento Médio Mensal")
                ticket_medio = st.text_input("Ticket Médio")
                tipo_produto = st.selectbox("Tipo de Produto", ["Produto A", "Produto B", "Produto C"])
                produtos_vendidos = st.text_input("Produtos Vendidos")
                telefone_suporte = st.text_input("Telefone de Suporte")
                telefone_contato = st.text_input("Telefone de Contato")
                site = st.text_input("Site")
                nome_representante = st.text_input("Nome do Representante Legal")
                mae_representante = st.text_input("Nome da mãe do Representante Legal")
                telefone_representante = st.text_input("Telefone do Representante Legal")
                cpf_representante = st.text_input("CPF do Representante Legal")
                nascimento_representante = st.date_input("Data de nascimento")

                submit_button3 = st.form_submit_button(label="Finalizar Cadastro", use_container_width=True)

            if submit_button3:
                st.success("Cadastro finalizado com sucesso!")
                st.session_state.register_step = 1  # Resetar o passo ao finalizar

                if senha != confirmar_senha:
                    st.error("As senhas não coincidem!")
                elif username in user_db:
                    st.error("Usuário já existe!")
                # else:
                #     if register(username, senha, nome_representante):
                #         st.success("Usuário registrado com sucesso! Agora você pode fazer login.")
                #         st.experimental_set_query_params(mode="login")
                #     else:
                #         st.error("Erro ao registrar o usuário.")

    elif auth_mode == "forgot_password":
        st.write("# Recuperação de Senha")

        username = st.text_input("Digite seu usuário para recuperação de senha")
        reset_button = st.button("Enviar Instruções")

        if reset_button:
            if username in user_db:
                st.success("Instruções de recuperação de senha enviadas para o email cadastrado (simulado).")
            else:
                st.error("Usuário não encontrado.")
        st.markdown("[Voltar ao login](?mode=login)")