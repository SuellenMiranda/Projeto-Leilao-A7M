<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $name = filter_input(INPUT_POST, 'Name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'Email', FILTER_VALIDATE_EMAIL);
    $subject = filter_input(INPUT_POST, 'Subject', FILTER_SANITIZE_STRING);
    $message = $_POST['Message'];

    // Configurar o email de destino
    $to = "suellen.org@example.com";

    // Configurar o assunto do email
    $email_subject = "Novo contato de $name sobre $subject";

    // Construir o corpo do email
    $email_body = "Você recebeu uma nova mensagem de $name.\n\n".
                    "Email: $email\n\n".
                    "Mensagem:\n$message";

    // Enviar o email
    mail($to, $email_subject, $email_body);

    // Redirecionar o usuário de volta para a página do formulário
    header('Location: /contato.html?enviado=1');
    exit;

}
