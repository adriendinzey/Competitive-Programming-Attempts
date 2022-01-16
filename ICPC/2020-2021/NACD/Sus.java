import java.util.*;
import java.io.*;

class Vertex {

    private String label;
    private boolean beingVisited;
    private boolean visited;
    private List<Vertex> adjacencyList;
    public boolean clear; 

    public Vertex(String label) {
        this.label = label;
        this.adjacencyList = new ArrayList<>();
        clear=false;
    }

    public void addNeighbor(Vertex adjacent) {
        this.adjacencyList.add(adjacent);
    }
    //getters and setters
    public void setBeingVisited(boolean b){
        beingVisited=b;
    }
    public boolean isBeingVisited(){
        return beingVisited;
    }
    public void setVisited(boolean b){
        visited=b;
    }
    public boolean isVisited(){
        return visited;
    }
    public List<Vertex> getAdjacencyList(){
        return adjacencyList;
    }

}
class Graph {

    private List<Vertex> vertices;

    public Graph() {
        this.vertices = new ArrayList<>();
    }

    public void addVertex(Vertex vertex) {
        this.vertices.add(vertex);
    }

    public void addEdge(int from, int to){
        addEdge(vertices.get(from), vertices.get(to));
    }

    public void addEdge(Vertex from, Vertex to) {
        from.addNeighbor(to);
    }

    public boolean hasCycle(Vertex sourceVertex) {
        sourceVertex.setBeingVisited(true);
    
        for (Vertex neighbor : sourceVertex.getAdjacencyList()) {
            if (neighbor.isBeingVisited()) {
                // backward edge exists
                return true;
            } else if (!neighbor.isVisited() && hasCycle(neighbor)) {
                return true;
            }
        }
    
        sourceVertex.setBeingVisited(false);
        sourceVertex.setVisited(true);
        return false;
    }
    public boolean hasCycle() {
        for (Vertex vertex : vertices) {
            if (!vertex.isVisited() && hasCycle(vertex)) {
                return true;
            }
        }
        return false;
    }
}
public class Sus {
    public static void main(String[] args) throws Exception{
        //Scanner in = new Scanner(new File("in.txt"));
        Scanner in = new Scanner(System.in);
        int[] nums = stringToInt(in.nextLine());

        int n = nums[0];
        int k = nums[1];

        int[] vouches = new int[n+1];
        Graph g = new Graph();
        for (int i = 1; i <= n; i++) {
            int vouchList[]= stringToInt(in.nextLine());

            for (int v = 1; v < vouchList.length; v++) {

                if (i != vouchList[v]) {
                    g.addEdge(i, v);
                }

            }
        }
        
        boolean[] curr = new boolean[n+1];
        for (int i = 1; i <= n; i++) {
            if (vouches[i] >= k) {
                curr[i]=true;
            }
            else {
                curr[i]=false;
            }
        }
        boolean[] prev = new boolean[n+1];
    }

    public static int[] stringToInt(String s){
        String[] arr = s.split(" ");
        int [] intArr = new int[arr.length];
        for(int i=0;i<arr.length;i++){
            intArr[i]=Integer.parseInt(arr[i]);
        }
        return intArr;
    }



}