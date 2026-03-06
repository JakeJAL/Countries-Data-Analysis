import matplotlib.pyplot as plt

def draw_languages(data):
    fig, ax = plt.subplots()
    data['languages'].value_counts().iloc[:10].plot(ax=ax, kind='bar')
    plt.show()

def draw_un_members(data):
    fig, ax = plt.subplots()
    data['unMember'].value_counts().plot(ax=ax, kind='bar')
    plt.show()