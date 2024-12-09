class Network:
    """
    Classe che rappresenta una rete basata su un protocollo di routing Distance Vector.
    
    Ogni nodo mantiene una tabella di routing che viene aggiornata iterativamente 
    attraverso lo scambio di informazioni con i nodi vicini.

    Attributi:
        nodes (list): Lista dei nodi nella rete.
        graph (dict): Rappresentazione del grafo con i costi tra i nodi {nodo: {vicino: costo}}.
        routing_tables (dict): Tabelle di routing per ogni nodo {nodo: {destinazione: (costo, prossimo_nodo)}}.
    """

    def __init__(self, nodes):
        """
        Inizializza una nuova istanza della rete.

        Args:
            nodes (list): Lista dei nodi che compongono la rete.
        """
        self.nodes = nodes  # Lista dei nodi nella rete
        self.graph = {node: {} for node in nodes}  # Grafo dei costi tra nodi
        self.routing_tables = {node: {n: (float('inf'), None) for n in nodes} for node in nodes}

    def add_link(self, node1, node2, cost):
        """
        Aggiunge un collegamento bidirezionale tra due nodi con un costo specificato.

        Args:
            node1 (str): Primo nodo del collegamento.
            node2 (str): Secondo nodo del collegamento.
            cost (int): Costo del collegamento.
        """
        self.graph[node1][node2] = cost
        self.graph[node2][node1] = cost

    def initialize_tables(self):
        """
        Inizializza le tabelle di routing per tutti i nodi:
        - La distanza di un nodo a se stesso è 0.
        - La distanza verso tutti gli altri nodi è inizialmente infinita.
        """
        for node in self.nodes:
            self.routing_tables[node][node] = (0, node)  # Distanza a se stesso è 0

    def update_routing(self):
        """
        Aggiorna le tabelle di routing usando il protocollo Distance Vector.
        Ogni nodo confronta i percorsi esistenti con nuove rotte calcolate attraverso i vicini.

        Returns:
            bool: True se almeno una tabella è stata aggiornata, False altrimenti.
        """
        updated = False
        for node in self.nodes:  # Itera su ogni nodo della rete
            for neighbor, cost in self.graph[node].items():  # Per ogni vicino del nodo
                for dest, (current_cost, _) in self.routing_tables[neighbor].items():  # Per ogni destinazione nella tabella del vicino
                    new_cost = cost + current_cost  # Calcola il nuovo costo del percorso
                    if new_cost < self.routing_tables[node][dest][0]:  # Se il nuovo percorso è più breve
                        self.routing_tables[node][dest] = (new_cost, neighbor)  # Aggiorna la tabella di routing
                        updated = True  # Segnala che è avvenuto un aggiornamento
        return updated

    def simulate(self):
        """
        Simula il protocollo di routing Distance Vector.
        - Inizializza le tabelle di routing.
        - Aggiorna iterativamente le tabelle fino a convergenza.
        - Stampa lo stato delle tabelle di routing a ogni iterazione.
        """
        self.initialize_tables()
        iteration = 0
        while True:
            print(f"\n--- Iterazione {iteration} ---")
            for node, table in self.routing_tables.items():
                print(f"Tabella di routing per {node}: {table}")
            if not self.update_routing():  # Interrompe quando non ci sono più aggiornamenti
                break
            iteration += 1


# Creazione della rete
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
network = Network(nodes)

# Aggiunta dei link con i relativi costi
network.add_link('A', 'B', 2)
network.add_link('A', 'D', 6)
network.add_link('A', 'E', 3)
network.add_link('B', 'E', 1)
network.add_link('B', 'C', 2)
network.add_link('C', 'E', 3)
network.add_link('C', 'H', 1)
network.add_link('D', 'E', 2)
network.add_link('E', 'F', 3)
network.add_link('E', 'H', 4)
network.add_link('F', 'G', 2)
network.add_link('G', 'H', 2)


# Simulazione del protocollo
network.simulate()