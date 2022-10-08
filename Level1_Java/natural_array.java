import java.util.Arrays;

public class natural_array {
    public static int[] solution(long n) {
        int size = String.valueOf(n).length();
        int[] answer = new int[size];
        int[] temp;
        for (int i = 0; i < size; i++) {
            answer[i] = (int)(n%10);
            n/=10;
        }
        return answer;
    }

    public static void main(String[] args){
        System.out.println(Arrays.toString(solution(12345)));
    }
}
