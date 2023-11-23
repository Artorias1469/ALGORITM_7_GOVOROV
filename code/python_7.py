#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import heapq

def count_characters(sentence):
    char_count = {}
    for char in sentence:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def build_huffman_tree(frequencies):
    heap = []
    buffer_fs = set()

    for key in frequencies:
        heapq.heappush(heap, (frequencies[key], key))

    while len(heap) > 1:
        f1, i = heapq.heappop(heap)
        f2, j = heapq.heappop(heap)
        fs = f1 + f2
        ord_val = ord('a')
        fl = str(fs)

        while fl in buffer_fs:
            letter = chr(ord_val)
            fl = str(fs) + " " + letter
            ord_val += 1

        buffer_fs.add(fl)
        frequencies[fl] = {f"{x}": frequencies[x] for x in [i, j]}
        del frequencies[i], frequencies[j]
        heapq.heappush(heap, (fs, fl))

    return frequencies


def text_to_binary(text):
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result


def coding_huffman(sentence, dictionary):
    replaced_sentence = ''.join([dictionary[char] if char in dictionary else char for char in sentence])
    return replaced_sentence


def binary_to_text(binary_text):
    binary_values = binary_text.split()
    text_result = ''.join(chr(int(value, 2)) for value in binary_values)
    return text_result


if __name__ == "__main__":
    user_input = input("Введите предложение: ")

    char_frequencies = count_characters(user_input)
    print("Результат подсчета вхождений каждого символа:")
    for char, count in char_frequencies.items():
        print(f"Символ '{char}': {count} раз")

    huffman_tree = build_huffman_tree(char_frequencies)
    print("\nДерево Хаффмана:")
    print(huffman_tree)

    coded_sentence = coding_huffman(user_input, huffman_tree)
    print("\nЗакодированное предложение:")
    print(coded_sentence)

    binary_text = text_to_binary(user_input)
    print("\nБинарное представление текста:")
    print(binary_text)

    decoded_text = binary_to_text(binary_text)
    print("\nРаскодированный текст:")
    print(decoded_text)