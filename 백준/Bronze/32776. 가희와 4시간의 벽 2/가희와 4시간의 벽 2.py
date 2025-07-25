def func(s_ab, m_ab):
    if s_ab <= m_ab or s_ab <= 240:
        print('high speed rail')
    else:
        print('flight')

s_ab = int(input())
m_a, f_ab, m_b = map(int, input().split())

func(s_ab, m_a + f_ab + m_b)