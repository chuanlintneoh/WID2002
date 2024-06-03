# Question 4 (animated)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def a(x):
  return np.where((x >= 0) & (x <= np.pi), np.pi, 0)
def b(x):
  return np.exp(x)
def c(x):
  return x/2
def lecture_example(x):
  return x

domain_a = np.linspace(-np.pi, np.pi, 100)
domain_b = np.linspace(-np.pi, np.pi, 100)
domain_c = np.linspace(0, 2*np.pi, 100)
domain_example = np.linspace(-np.pi, np.pi, 100)

def fourier_series(a0, an_func, bn_func, x, n):
  result = a0
  for num_terms in range(1, n + 1):
    result += an_func(num_terms) * np.cos(num_terms*x) + bn_func(num_terms) * np.sin(num_terms*x)
  return result

def an_b(n):
  return (1/np.pi)*(
    (np.exp(np.pi) - np.exp(-np.pi))*(((-1)**n)/(n**2)) +
    (np.exp(-np.pi) - np.exp(np.pi))*(((-1)**n)/((n**2)*(n**2 + 1)))
    )

def bn_a(n):
  return (1-(-1)**n)/n
def bn_b(n):
  return (1/np.pi)*(
    ((np.exp(np.pi)*(-1)**(n+1))/n) -
    ((np.exp(np.pi)*(-1)**(n+1))/(n*(n**2 + 1))) -
    ((np.exp(-np.pi)*(-1)**(n+1))/n) +
    ((np.exp(-np.pi)*(-1)**(n+1))/(n*(n**2 + 1)))
    )
def bn_c(n):
  return -1/n
def bn_example(n):
  return (2/n) * (-1)**(n+1)

animations = [
  {
    'func': a,
    'domain': domain_a,
    'title': '$f(x) = 0, \pi$',
    'fourier_series_title': '$f(x) = \\frac{\pi}{2} + \sum_{n=1}^{\infty} \\frac{2}{n} sin(nx)$',
    'a0_constant': np.pi/2,
    'an_func': lambda n: 0,
    'bn_func': bn_a
  },
  {
    'func': b,
    'domain': domain_b,
    'title': '$f(x) = e^x$',
    # 'fourier_series_title': '$f(x) = \\frac{\exp(\pi) - \exp(-\pi)}{2\pi} + \sum_{n=1}^{\infty} \left( \\frac{1}{\pi} \left( (\\exp(\pi) - \\exp(-\pi)) \\frac{(-1)^n}{n^2} + (\\exp(-\pi) - \\exp(\pi)) \\frac{(-1)^n}{n^2(n^2 + 1)} \\right) \\cos(nx) + \\frac{1}{\pi} \left( \\frac{\\exp(\pi)(-1)^{n+1}}{n} - \\frac{\\exp(\pi)(-1)^{n+1}}{n(n^2 + 1)} - \\frac{\\exp(-\pi)(-1)^{n+1}}{n} + \\frac{\\exp(-\pi)(-1)^{n+1}}{n(n^2 + 1)} \\right) \\sin(nx) \\right)$',
    'fourier_series_title': 'hidden...',
    'a0_constant': (np.exp(np.pi) - np.exp(-np.pi)) / (2*np.pi),
    'an_func': an_b,
    'bn_func': bn_b
  },
  {
    'func': c,
    'domain': domain_c,
    'title': '$f(x) = \\frac{x}{2}$',
    'fourier_series_title': '$f(x) = \\frac{\pi}{2} + \sum_{n=1}^{\infty} -\\frac{1}{n} sin(nx)$',
    'a0_constant': np.pi/2,
    'an_func': lambda n: 0,
    'bn_func': bn_c
  },
  {
    'func': lecture_example,
    'domain': domain_example,
    'title': '$f(x) = x$',
    'fourier_series_title': '$f(x) = \sum_{n=1}^{\infty} (\\frac{2}{k} (-1)^{n+1} sin(nx))$',
    'a0_constant': 0,
    'an_func': lambda n: 0,
    'bn_func': bn_example
  }
]
num_terms = 1000

def animate_graph(animation_choice):
  selected_animation = animations[animation_choice]
  
  func = selected_animation['func']
  domain = selected_animation['domain']
  title = selected_animation['title']
  fourier_series_title = selected_animation['fourier_series_title']
  a0_constant = selected_animation['a0_constant']
  an_func = selected_animation['an_func']
  bn_func = selected_animation['bn_func']
  
  fig, ax = plt.subplots(figsize=(10, 5))
  
  def update(frame):
    ax.cla()
    ax.plot(domain, func(domain), color='black', label=title)
    ax.plot(domain, fourier_series(a0_constant, an_func, bn_func, domain, frame), color='red', label='Fourier Approximation')
    ax.set_title(f'Fourier Series Approximation: {fourier_series_title}')
    ax.grid()
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.axhline(0, color='black', lw=1)
    ax.axvline(0, color='black', lw=1)
    ax.legend()
  
  anim = FuncAnimation(fig, update, frames=range(1, num_terms + 1), interval=200)
  
  plt.tight_layout()
  plt.show()

user_choice = int(input("Enter the number corresponding to the animation (0: a, 1: b, 2: c, 3: lecture_example): "))
animate_graph(user_choice)