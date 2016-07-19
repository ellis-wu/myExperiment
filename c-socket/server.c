#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <strings.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>

const int size = 327680;
const int loop = 50000000; //max 2147483647

void *connection_handler(void *);

int main()
{
    int sockfd, clientfd;
    struct sockaddr_in dest;
    struct sockaddr_in client_addr;
    socklen_t addrlen = sizeof(client_addr);
    pthread_t thread_id;

    /* create sockett */
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        printf("Creating socket fail\n");
    } else {
        /* initialize structure dest */
        bzero(&dest, sizeof(dest));
        dest.sin_family = AF_INET;
        dest.sin_port = htons(8889);
        /* this line is different from client */
        dest.sin_addr.s_addr = INADDR_ANY;

        /* Assign a port number to socket */
        if (bind(sockfd, (struct sockaddr*)&dest, sizeof(dest)) == -1) {
            printf("bind fail.\n");
        } else {
            /* make it listen to socket with max 20 connections */
            if (listen(sockfd, 100) == -1) {
                printf("Listening fail\n");
            } else {
                while (1) {
                    clientfd = accept(sockfd, (struct sockaddr*)&client_addr, &addrlen);
                    pthread_create(&thread_id, NULL, connection_handler, (void*) &clientfd);
                }
                //pthread_join(thread_id, NULL);
                //pthread_detach(thread_id);
            }
        }
    }

    /* close(server) , but never get here because of the loop */
    close(sockfd);
    return 0;
}

void *connection_handler(void *socket_desc)
{
    int sock = *(int*)socket_desc;
    int read_size;
    char buffer[20] = "Hi client! ";
    char buffer1[10];

    /* Receive message from the client and print to screen */
    while ( (read_size = recv(sock, buffer1, sizeof(buffer1), 0)) > 0) {
        printf("[%d] receive from client: %s\n", sock, buffer1);

        /* Loading generate */
        int *ptr = (int *) calloc(sizeof(int) * size * 5, sizeof(int));
        int i, sum = 0;
        for (i = 1; i <= loop; i++) {
            sum += i;
        }
        //sleep(2);
        free(ptr);

        /* Send message to client */
        send(sock, buffer, sizeof(buffer), 0);
    }

    if (read_size == 0) {
        puts("Client disconnected");
        fflush(stdout);
    }
    else if(read_size == -1) {
        perror("recv failed");
    }

    return 0;
}

