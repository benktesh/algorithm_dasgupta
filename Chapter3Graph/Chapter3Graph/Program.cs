using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chapter3Graph
{
	class Program
	{
		class Graph
		{
			private int V; //number of verticies
			private LinkedList<int>[] adj; //array of linkedList 

			public Graph(int v)
			{
				V = v; 
				adj = new LinkedList<int>[v];
				for (int i = 0; i < v; i++)
				{
					adj[i] = new LinkedList<int>();
				}
			}

			public void AddEdge(int v, int w)
			{
				adj[v].AddLast(w);
			}


			public void DFSUtil(int v, Boolean[] visited)
			{
				visited[v] = true;
				Console.WriteLine("Just Visted " + v + " .");
				foreach (var node in adj[v])
				{
					if (!visited[node])
					{
						DFSUtil(node, visited);
					}					
				}
			}
			public void DFS()
			{
				Boolean[] visited = new Boolean[V];
				foreach (int v in Enumerable.Range(0,V))
				{
					if (!visited[v])
					{
						DFSUtil( v, visited );
					}
					
				}
				
			}
			public void DFS(int v)
			{
				Boolean[] visited = new Boolean[V];
				DFSUtil(v, visited);
			}

			private bool IsCyclicUtil(int v, bool[] visited, bool[] recStack)
			{
				if (!visited[v])
				{
					visited[v] = true;
					recStack[v] = true;

					foreach (var node in adj[v])
					{
						if (!visited[node] && IsCyclicUtil( node, visited, recStack))
						{
							return true;
						}
						else if (recStack[node])
							return true; 
					}
				}
				recStack[v] = false;
				return false; 
			}

			public bool IsCyclic()
			{
				Boolean[] visited = new Boolean[V];
				Boolean[] recStack = new Boolean[V];

				for (int i = 0; i < V; i++)
				{
					if ( IsCyclicUtil( i, visited, recStack))
						return true; 
				}
				return false; 

			}

			public void BFS(int s)
			{
				Boolean[] visited = new Boolean[V];
				Queue<int> queue = new Queue<int>();
				visited[s] = true;
				queue.Enqueue(s);

				while (queue.Count() != 0)
				{
					s = queue.Dequeue();
					Console.WriteLine("> " + s + " ");

					foreach (var node in adj[s])
					{
						if (!visited[node])
						{
							visited[node] = true;
							queue.Enqueue(node);
						}
						
					}
				} 
			}
		}


		static void Main( string[] args )
		{

			var graph = new Graph(4);
			
			graph.AddEdge(0, 1);

			graph.AddEdge( 0, 2 );
graph.AddEdge(1, 2);
graph.AddEdge(2, 0);
			graph.AddEdge(2, 3);
graph.AddEdge(3, 3);

			graph.DFS();
			Console.WriteLine("BFS :"); graph.BFS(2);


			Console.WriteLine("OK");

			
		}
	}
}
