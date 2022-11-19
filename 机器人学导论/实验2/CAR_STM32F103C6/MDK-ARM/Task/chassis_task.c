#include "chassis_task.h"


void ChassisTask(void const * argument)
{
  /* USER CODE BEGIN ChassisTask */

	HAL_TIM_PWM_Start(&htim1, TIM_CHANNEL_4);
  /* Infinite loop */
  while(1)
  {
		set_servo(2000);			//对应90°
    osDelay(1000);				//表示延迟1000ms
		
  }
  /* USER CODE END ChassisTask */
}


void set_servo(uint16_t pwm_value)
{
	__HAL_TIM_SET_COMPARE(&htim1, TIM_CHANNEL_4, pwm_value);
}



