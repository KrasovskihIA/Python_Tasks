"""
Необходимо написать универсальную основу для представления ненаправленных связных графов и поиска в них 
кратчайших маршрутов. Далее, этот алгоритм предполагается применять для прокладки маршрутов: на картах,
в метро и так далее.
Для универсального описания графов, вам требуется объявить в программе следующие классы:

Vertex - для представления вершин графа (на карте это могут быть: здания, остановки, достопримечательности и т.п.);
Link - для описания связи между двумя произвольными вершинами графа (на карте: маршруты, время в пути и т.п.);
LinkedGraph - для представления связного графа в целом (карта целиком).
"""

import math


class Vertex:
    def __init__(self):
        self._links = []
        self._vertexs = {self}

    @property
    def links(self):
        return self._links

    def add_link(self, links):
        if not isinstance(links, Link):
            raise ValueError
        if links.v1 not in self._vertexs:
            self._links.append(links)
            self._vertexs.add(links.v1)
        elif links.v2 not in self._vertexs:
            self._links.append(links)
            self._vertexs.add(links.v2)


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Link:
    def __init__(self, v1, v2, dist=1):
        self.v1 = v1
        self.v2 = v2
        self.dist = dist

    @property
    def v1(self):
        return self._v1

    @v1.setter
    def v1(self, v):
        #if isinstance(v, Vertex):
            #raise ValueError
        self._v1 = v

    @property
    def v2(self):
        return self._v2

    @v2.setter
    def v2(self, v):
        #if isinstance(v, Vertex):
            #raise ValueError
        self._v2 = v

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, dist):
        if type(dist) != int:
            raise ValueError
        self._dist = dist

    def get_other(self, v):
        if v == self.v1:
            return self.v2
        return self.v2


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2, dist)


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []
        self.links_true = set()

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if not (link.v1, link.v2) in self.links_true and not (link.v2, link.v1) in self.links_true:
            link.v1.add_link(link)
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            self.links_true.add((link.v1, link.v2))

    def find_link(self, v1, v2):
        for i in self._links:
            if (v1 == i.v1 and v2 == i.v2) or (v1 == i.v2 and v2 == i.v1):
                return i


    @staticmethod
    def arg_min(T, S):
        amin = -1
        m = math.inf  # максимальное значение
        for i, t in T.items():
            if t < m and i not in S:
                m = t
                amin = i

        return amin

    def find_path(self, start_v, stop_v):
        N = len(self._vertex)  # число вершин в графе
        T = dict(zip(self._vertex, (math.inf for _ in range(N))))

        v = start_v
        S = {v}
        T[v] = 0  # нулевой вес для стартовой вершины
        M = dict(zip(self._vertex, (0 for _ in range(N)))) # оптимальные связи между вершинами

        while v != -1:
            for i in v.links:
                w = T[v] + i.dist
                j = i.get_other(v)
                if w < T[j]:
                    T[j] = w
                    M[j] = v

            v = self.arg_min(T, S)  # выбираем следующий узел с наименьшим весом
            if v != -1:  # выбрана очередная вершина
                S.add(v)  # добавляем новую вершину в рассмотрение

        # формирование оптимального маршрута:
        start = start_v
        end = stop_v
        P = [end]
        s = []
        while end != start:
            end = M[P[-1]]
            P.append(end)
            s.append(self.find_link(P[-1], P[-2]))

        return P[::-1], s