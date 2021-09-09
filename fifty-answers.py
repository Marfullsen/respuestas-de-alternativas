respuestas = ['1. A B C ●', '2. ● B C D', '3. ● B C D', '4. A ● C D', '5. A B C ●', '6. A B ● D', '7. A B ● D', '8. A ● C D', '9. A ● C D', '10. A ● C D', '11. ● B C D', '12. A B ● D', '13. ● B C D', '14. A B C ●', '15. ● B C D', '16. A B C ●', '17. ● B C D', '18. ● B C D', '19. A B ● D', '20. ● B C D', '21. ● B C D', '22. A B C ●', '23. A B ● D', '24. A ● C D', '25. A B ● D']
respuestas += ['26. A ● C D', '27. A B C ●', '28. A B ● D', '29. A B ● D', '30. A B C ●', '31. A ● C D', '32. A ● C D', '33. A B ● D', '34. ● B C D', '35. A B C ●', '36. A B ● D', '37. A B ● D', '38. ● B C D', '39. A ● C D', '40. A B C ●', '41. A B C ●', '42. A B ● D', '43. A B C ●', '44. A B ● D', '45. ● B C D', '46. A ● C D', '47. ● B C D', '48. A ● C D', '49. A B ● D', '50. A B C ●']

def faltante(sublista):
    alternativas = ['A', 'B', 'C', 'D']
    for alternativa in alternativas:
        if alternativa not in sublista:
            return alternativa
    return 'Error'

only_num = lambda s: ''.join([i for i in s if i.isdigit()])

for enunciado in respuestas:
    num = f'{only_num(enunciado)}'
    letra = faltante(enunciado)
    print(f'{num}-{letra}')
