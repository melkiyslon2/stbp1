Водолазський Микола Анатолійович КН-М922в використання мнемонічних фраз для формування ключів шифрування.
Передмова
Зберігати публічний та приватний ключі "як вони є" на не-електронному носії незручно, тому, 100% безпечного каналу їх передачі та бекапу не існує. Щоб зробити це можливим, треба використовувати принцип генерації цих ключів - вони залежать від генератора псевдовипадкових чисел. Але ми знаємо, що два генератора псевдовипадкових чисел з однаковим початковим значенням (seed) генерують однакові послідовності (тому вони й є псевдо-випадковими генераторами). Для створення безпечного seed'a з зрозумілого людині тексту, використовується алгоритм bip39.
Завдання
Використовуючи алгоритм bip39, створити seed генератора псевдовипадкових чисел за допомогою мнемонічної фрази та стосовні ключі шифрування.
Зашифрувати текст
Використовуючи раніше створену мнемонічну фразу, відновити ключі шифрування на дешифрувати текст. Вдосконалитись, що оригінальний та дешифрований тексти однакові.
