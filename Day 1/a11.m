file = uiimport('input.txt');
tStart = cputime;
found = 0;
for i = 1:200
    for j = 1+i:200
        if (file.input(i) + file.input(j)) == 2020
            found = 1;
            break
        end
    end
    if found == 1
        break
    end
end

file.input(i) * file.input(j)
found = 0;

for i = 1:200
    for j = 1+i:200
        for k = 1+j:200
            if (file.input(i) + file.input(j) + file.input(k)) == 2020
                found = 1
                break
            end
        end
        if found == 1
            break
        end
    end
    if found == 1
        break
    end
end
file.input(i) * file.input(j) * file.input(k)

tEnd = cputime - tStart