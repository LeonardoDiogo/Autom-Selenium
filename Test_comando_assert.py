# assert True

# num_esperado = 2
# num_obtido = 2
# assert num_esperado == num_obtido, f"Esperado {num_esperado}. Atual {num_obtido}"


text_esperado = "Selenium Webdrive"
text_obtido = "Selenium webdrive"
assert text_esperado.lower() == text_obtido.lower(
), f"Esperado {text_esperado}. Atual {text_obtido}"
