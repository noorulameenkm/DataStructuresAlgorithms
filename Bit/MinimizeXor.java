package Bit;

public class MinimizeXor {
    public int minimizeXor(int num1, int num2) {
        int x = num1;

        int currentSetBitCount = setBitCount(x);
        int targetSetBitCount = setBitCount(num2);

        int bitPosition = 0;
        if(currentSetBitCount < targetSetBitCount) {
            while(currentSetBitCount < targetSetBitCount) {
                if(!isBitSet(x, bitPosition)) {
                    x = setBit(x, bitPosition);
                    currentSetBitCount++;
                }

                bitPosition++;
            }
        } else if(currentSetBitCount > targetSetBitCount) {
            while(currentSetBitCount > targetSetBitCount) {
                if(isBitSet(x, bitPosition)) {
                    x = unsetBit(x, bitPosition);
                    currentSetBitCount--;
                }

                bitPosition++;
            }
        }

        return x;
    }

    private boolean isBitSet(int num, int bitPosition) {
        num = num & (1 << bitPosition);
        return num > 0;
    }


    private int setBit(int num, int bitPosition) {
        return num | (1 << bitPosition);
    }

    private int unsetBit(int num, int bitPosition) {
        return num & (~(1 << bitPosition));
    }


    private int setBitCount(int num) {
        int count = 0;
        while(num > 0) {
            count += num & 1;
            num >>= 1;
        }

        return count;
    }

    public static void main(String[] args) {
        MinimizeXor solution = new MinimizeXor();
        System.out.println(solution.minimizeXor(3, 5));
        System.out.println(solution.minimizeXor(1, 12));
    }
}
