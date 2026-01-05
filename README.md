# Conversor de Imagens para PDF

Aplicativo simples com interface gráfica para unir múltiplas imagens em um único arquivo PDF.

## 📋 Descrição

Este aplicativo permite selecionar várias imagens (PNG, JPG, JPEG, WEBP) e convertê-las em um único documento PDF, com cada imagem representando uma página.

## ✨ Funcionalidades

- Interface gráfica intuitiva usando Tkinter
- Suporte para múltiplos formatos de imagem (PNG, JPG, JPEG, WEBP)
- Conversão automática para RGB
- Seleção de múltiplos arquivos de uma vez
- Escolha do local e nome do PDF de saída

## 🔧 Tecnologias Utilizadas

- Python 3.x
- Tkinter (interface gráfica)
- Pillow/PIL (processamento de imagens)
- PyInstaller (geração do executável)

## 📦 Instalação

### Executável (Windows)

Baixe o arquivo `app.exe` e execute diretamente. Não é necessária instalação do Python.

### Executando do código-fonte

1. Clone o repositório
2. Instale as dependências:
```bash
pip install pillow
```

3. Execute o aplicativo:
```bash
python app.py
```

## 🚀 Como Usar

1. Abra o aplicativo
2. Clique em "Selecionar imagens e gerar PDF"
3. Selecione uma ou mais imagens (use Ctrl para seleção múltipla)
4. Escolha o local e nome para salvar o PDF
5. Aguarde a mensagem de sucesso

## 🔨 Gerando o Executável

Para gerar o executável usando PyInstaller:
```bash
# Instalar PyInstaller
pip install pyinstaller

# Gerar executável
pyinstaller app.spec
```

O executável será gerado na pasta `dist/`.

### Configuração do PyInstaller

O arquivo `app.spec` está configurado para:
- Gerar um executável único (--onefile)
- Modo windowed sem console (console=False)
- Compressão UPX habilitada
- Nome do executável: `app.exe`

## 📝 Notas

- As imagens são convertidas para RGB automaticamente para garantir compatibilidade com o formato PDF
- A ordem das imagens no PDF segue a ordem de seleção
- O aplicativo não possui limite de imagens, mas PDFs muito grandes podem demorar para processar

## 🐛 Solução de Problemas

**Erro ao abrir imagens**: Verifique se os arquivos não estão corrompidos e são de fatos imagens válidas.

**Executável não abre**: Em alguns sistemas Windows, o antivírus pode bloquear executáveis gerados com PyInstaller. Adicione uma exceção se necessário.

## 📄 Licença

Este projeto está disponível para uso livre.

## 👤 Autor

Desenvolvido em Python com ❤️
