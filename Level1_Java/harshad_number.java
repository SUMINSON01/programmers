public class harshad_number {
    public static boolean solution(int x) {
        boolean answer = false;
        int sum = 0;
        int n = x;
        int size = String.valueOf(x).length();
        for(int i = 0; i < size; i++){
            sum += (n%10);
            n/=10;
        }

        if(x % sum == 0)
            answer = true;
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(10));
    }
}

