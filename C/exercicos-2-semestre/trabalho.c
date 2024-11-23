#include <stdio.h>
#include <stdlib.h>

// Definição da estrutura de um nó da árvore
struct Node {
    int data;
    struct Node *left, *right;
};

// Função para criar um novo nó
struct Node* newNode(int item) {
    struct Node* temp = (struct Node*)malloc(sizeof(struct Node));
    temp->data = item;
    temp->left = temp->right = NULL;
    return temp;
}

// Função para inserir um novo nó na árvore de busca
struct Node* insert(struct Node* node, int data) {
    if (node == NULL) {
        return newNode(data);
    }

    if (data < node->data) {
        node->left = insert(node->left, data);
    } else if (data > node->data) {
        node->right = insert(node->right, data);
    }

    return node;
}

// Função para realizar a busca de um valor na árvore
struct Node* search(struct Node* root, int key) {
    if (root == NULL || root->data == key)
        return root;

    if (key < root->data)
        return search(root->left, key);

    return search(root->right, key);
}

// Função para exibir a árvore em ordem (in-order traversal)
void inOrder(struct Node* root) {
    if (root != NULL) {
        inOrder(root->left);
        printf("%d ", root->data);
        inOrder(root->right);
    }
}

int main() {
    struct Node* root = NULL;
    int opcao, valor, busca;

    do {
        printf("\n\n1. Inserir\n2. Buscar\n3. Exibir (In-Order)\n4. Sair\nEscolha uma opcao: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Digite o valor a ser inserido: ");
                scanf("%d", &valor);
                root = insert(root, valor);
                printf("Valor inserido!\n");
                break;

            case 2:
                printf("Digite o valor a ser buscado: ");
                scanf("%d", &busca);
                if (search(root, busca)) {
                    printf("Valor encontrado!\n");
                } else {
                    printf("Valor nao encontrado.\n");
                }
                break;

            case 3:
                printf("Exibindo arvore em ordem: ");
                inOrder(root);
                printf("\n");
                break;

            case 4:
                printf("Saindo...\n");
                break;

            default:
                printf("Opcao invalida.\n");
        }
    } while (opcao != 4);

    return 0;
}