#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <strings.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <iostream>
#include <sys/time.h>

double time_diff(struct timeval x , struct timeval y);

int main()
{
    int sockfd;
    struct sockaddr_in dest;
    char buffer[128];
    char resp[10]="start";
    struct timeval before , after;
    gettimeofday(&before , NULL);

    /* create socket */
    sockfd = socket(PF_INET, SOCK_STREAM, 0);

    /* initialize value in dest */
    bzero(&dest, sizeof(dest));
    dest.sin_family = PF_INET;
    dest.sin_port = htons(8889);
    dest.sin_addr.s_addr = inet_addr("10.21.20.105");

    /* Connecting to server */
    connect(sockfd, (struct sockaddr*)&dest, sizeof(dest));

    /* Send message to server */
    send(sockfd,resp,sizeof(resp),0);

    /* Receive message from the server and print to screen */
    bzero(buffer, 128);
    recv(sockfd, buffer, sizeof(buffer), 0);

    gettimeofday(&after , NULL);
    printf("[ %.03f ms ] " , time_diff(before , after) );
    printf("receive from server: %s\n", buffer);

    /* Close connection */
    close(sockfd);

    return 0;
}

double time_diff(struct timeval x, struct timeval y)
{
    double x_ms , y_ms , diff;

    x_ms = (double)x.tv_sec*1000000 + (double)x.tv_usec;
    y_ms = (double)y.tv_sec*1000000 + (double)y.tv_usec;

    diff = (double)y_ms - (double)x_ms;

    return diff / 1000;
}

